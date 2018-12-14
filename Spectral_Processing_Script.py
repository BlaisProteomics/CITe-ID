import multiplierz.mgf as mgf
import copy, sys, os

global toler
toler = 0.03
diag_toler = 0.025

def recalibrate_mgf(datafiles, inhibitor = 'none'):
    inhibdict = {
        'THZ1-dtb':[1028.454, 474.3275, 521.1487, 994.468, 389.275, 346.233, 197.128, 431.285, 240.168],
        'JZ128-dtb':[1028.46, 988.54, 501.203, 457.302, 435.193, 389.276, 346.234, 240.171, 197.129]
    }
    subtract_list = []
    good_dic = False
    for key in inhibdict:
        if inhibitor == 'none':
            raise ValueError('No inhibitor name was provided')
        if inhibitor in key:
            mono_subtract_list = inhibdict[str(key)]
            good_dic = True
            break
    if not good_dic:
        raise ValueError("Inhibitor name doesn't match anything in the inhibitor dictionary")
    for ion in mono_subtract_list:
        subtract_list.append(ion)
        subtract_list.append(ion + 1.00794)
        subtract_list.append(ion + 2*1.00794)
    for single_file in datafiles:
        mgf_data = mgf.parse_to_generator(single_file)
        print "Parsing MGF"
        new_scans = []
        count = 0
        for entry in mgf_data:
            title = entry['title']
            pep_mass = entry['pepmass']
            has_charge = True
            try:
                charge = entry['charge']
            except:
                charge = 0
                has_charge = False
            try:
                cur_scan = entry['spectrum']
            except:
                cur_scan = [[1,1]]
            sub_scan = []
            good_scan = True
            if len(cur_scan) < 10:
                good_scan = False
            for mz, inten in cur_scan:
                add_it = True
                for val in subtract_list:
                    if abs(val-mz) <= toler:
                        add_it = False
                if add_it:
                    sub_scan.append((mz, inten))
            new_scans.append([title, pep_mass, charge, sub_scan, has_charge, good_scan])
        print "Subtracted all scans, tolerance: " + str(toler)
        print "Writing mgf..."
        filtered_mgf_file_name = single_file[:-4] + " %s subtracted.mgf" % inhibitor
        write_mgf(filtered_mgf_file_name, new_scans)

def write_mgf(file_name, scans):
#### This function writes a set of scans into a new mgf file ####
    out = file(file_name,'w')
    print >> out, "MASS=Monoisotopic"
    print >> out, "SEARCH=MIS"
    for title, pep_mass, charge, scan, has_charge, good_scan in scans:
        if good_scan:
            print >> out, "BEGIN IONS"
            print >> out, "TITLE=%s" % title
            print >> out, "PEPMASS=%.5f" % pep_mass
            if has_charge == True:
                print >> out, "CHARGE=%d+" % charge
            for (mz, intensity) in scan:
                print >> out, "%.4f\t%.4f" % (mz, intensity)
            print >> out, "END IONS\n"

if __name__ == '__main__':
    from multiplierz.mzGUI_standalone import file_chooser
    import sys
    import time
    
    start = time.clock()
    args = sys.argv
    
    if len(args) == 2:
        _, inhibitor = args
        print "Using inhibitor: %s" % (inhibitor)
    else:
        inhibitor = None
    datafiles = file_chooser("Choose mgf files:", mode = 'm', wildcard = '*.mgf')
    if datafiles:
        print 'Subtracting inhibitor fragment ions from spectra'
        recalibrate_mgf(datafiles, inhibitor = inhibitor)
    print "Runtime: " + str(time.clock() - start) 
