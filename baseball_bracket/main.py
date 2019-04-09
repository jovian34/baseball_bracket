from baseball_bracket.data_collect.get_current_rpi_wn import NolanRpiExpand
from baseball_bracket.data_collect.get_current_isr_bw import BoydsIsr
from baseball_bracket.data_collect.name_difference import change_mismatched_keys
from baseball_bracket.data_collect.name_difference import find_inconsistent_names
from baseball_bracket.conference.rank import ConferenceRank
from baseball_bracket.calculations.western_adjustment import WesternAdjustment
from baseball_bracket.calculations.conference_adjustment import ConferenceAdjustment
from baseball_bracket.data_collect.blank_auto_bids import blank_bids
from baseball_bracket.data_collect.get_auto_bids_wn import NolanAutoBid
from baseball_bracket.conference.auto_bid import AutoBid
from baseball_bracket.calculations.tourney_rank import TourneyRank
from baseball_bracket.calculations.group_adjustment import GroupAdjustment
from baseball_bracket.calculations.northern_adjustment import NorthernAdjustment
from baseball_bracket.calculations.regionals import Regionals
import json


def get_nolan_data():
    nolan_rpi = NolanRpiExpand()
    return nolan_rpi.get_nolan_dict()


def get_boyd_data(team_dict):
    boyd_isr = BoydsIsr()
    isr_dict = boyd_isr.get_isr_dict()
    isr_dict_fixed = change_mismatched_keys(isr_dict)
    if find_inconsistent_names(team_dict, isr_dict_fixed):
        raise ValueError('ISR names not correctly converted to RPI')
    return isr_dict_fixed


def calculate_conf_ranks(team_dict):
    conf_rank = ConferenceRank(team_dict)
    return conf_rank.update_team_dict_with_conf_ranks()


def calculate_western_adjustment(isr_dict, team_dict):
    west_adj = WesternAdjustment(team_dict, isr_dict)
    return west_adj.return_team_dict()


def calculate_conf_adjustment(team_dict):
    conf_adj = ConferenceAdjustment(team_dict)
    return conf_adj.return_team_dict()


def get_auto_bids():
    # auto_bids = NolanAutoBid()
    return blank_bids


def set_auto_bids(auto_bids, team_dict):
    auto_bids = AutoBid(team_dict, auto_bids)
    return auto_bids.return_team_dict()


def create_tourney_ranks(team_dict):
    tourney_rank = TourneyRank(team_dict)
    return tourney_rank.return_field()


def calculate_group_adjustments(team_dict):
    group_adjust = GroupAdjustment(team_dict)
    return group_adjust.return_team_dict()


def calculate_northern_adjustment(team_dict, isr_dict):
    north_adjust = NorthernAdjustment(team_dict, isr_dict)
    return north_adjust.return_team_data()


def create_regions(field, isr_dict, team_dict):
    regionals = Regionals(field, isr_dict, team_dict)
    regionals.print_field()


def export_team_dict(team_dict):
    with open('team_dict_w8.json', 'w') as outfile:
        json.dump(team_dict, outfile)


def export_isr_dict(isr_dict):
    with open('isr_dict_w8.json', 'w') as outfile:
        json.dump(isr_dict, outfile)


def export_auto_bids(auto_bids):
    with open('auto_bids_w8.json', 'w') as outfile:
        json.dump(auto_bids, outfile)


def main():
    team_dict = get_nolan_data()
    isr_dict = get_boyd_data(team_dict)
    auto_bids = get_auto_bids()
    team_dict = calculate_conf_ranks(team_dict)
    team_dict = calculate_western_adjustment(isr_dict, team_dict)
    team_dict = calculate_conf_adjustment(team_dict)
    team_dict = calculate_group_adjustments(team_dict)
    team_dict = calculate_northern_adjustment(team_dict, isr_dict)
    team_dict = set_auto_bids(auto_bids, team_dict)
    export_team_dict(team_dict)
    export_isr_dict(isr_dict)
    export_auto_bids(auto_bids)
    field = create_tourney_ranks(team_dict)
    create_regions(field, isr_dict, team_dict)


if __name__ == '__main__':
    main()







