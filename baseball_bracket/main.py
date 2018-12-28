from baseball_bracket.data_collect.get_current_rpi_wn import NolanRpiExpand
from baseball_bracket.data_collect.get_current_isr_bw import BoydsIsr
from baseball_bracket.data_collect.name_difference import change_mismatched_keys
from baseball_bracket.data_collect.name_difference import find_inconsistent_names


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







