from baseball_bracket.data_collect.get_current_rpi_wn import NolanRpiExpand
from baseball_bracket.data_collect.get_current_isr_bw import BoydsIsr
from baseball_bracket.data_collect.name_map import boyds_to_nolan


def change_mismatched_keys(isr):
    dict_fixed = {}
    for key, value in isr.items():
        if key not in boyds_to_nolan:
            dict_fixed[key] = value
        else:
            dict_fixed[boyds_to_nolan[key]] = value
    print(f'Size of ISR dict fixed inside of function is {len(dict_fixed)}')
    return dict_fixed


def find_inconsistent_names(rpi, isr):
    bad_isr_names = []
    good_names = []
    bad_rpi_names = []

    for key in isr:
        if key in rpi:
            good_names.append(key)
        else:
            bad_isr_names.append(key)

    for key in rpi:
        if key not in good_names:
            bad_rpi_names.append(key)

    if len(bad_isr_names) == len(bad_rpi_names) == 0:
        return False
    else:
        return True


def main():
    nolan_rpi = NolanRpiExpand()
    main_dict = nolan_rpi.get_nolan_dict()
    boyd_isr = BoydsIsr()
    isr_dict = boyd_isr.get_isr_dict()

    isr_dict_fixed = change_mismatched_keys(isr_dict)
    if find_inconsistent_names(main_dict, isr_dict_fixed):
        raise ValueError('ISR names not correctly converted to RPI')
    print('Names are now consistent.... Proceed to processing.')


if __name__ == '__main__':
    main()







