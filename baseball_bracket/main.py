from baseball_bracket.data_collect.get_current_rpi_wn import NolanRpiExpand
from baseball_bracket.data_collect.get_current_isr_bw import BoydsIsr
from baseball_bracket.data_collect.name_difference import change_mismatched_keys
from baseball_bracket.data_collect.name_difference import find_inconsistent_names
from baseball_bracket.conference.rank import ConferenceRank
from baseball_bracket.calculations.western_adjustment import WesternAdjustment
from baseball_bracket.calculations.conference_adjustment import ConferenceAdjustment
from baseball_bracket.data_collect.get_auto_bids_wn import NolanAutoBid
from baseball_bracket.conference.auto_bid import AutoBid
from baseball_bracket.calculations.tourney_rank import TourneyRank
from baseball_bracket.calculations.group_adjustment import GroupAdjustment


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
    auto_bids = NolanAutoBid()
    return auto_bids.return_auto_bid_dict()


def set_auto_bids(auto_bids, team_dict):
    auto_bids = AutoBid(team_dict, auto_bids)
    return auto_bids.return_team_dict()


def create_tourney_ranks(team_dict):
    tourney_rank = TourneyRank(team_dict)
    tourney_rank.print_field()


def calculate_group_adjustments(team_dict):
    group_adjust = GroupAdjustment(team_dict)
    return group_adjust.return_team_dict()


def main():
    team_dict = get_nolan_data()
    print(f"Stanford Adjusted RPI: {team_dict['STANFORD']['adjusted_rpi']}")
    isr_dict = get_boyd_data(team_dict)
    auto_bids = get_auto_bids()
    team_dict = calculate_conf_ranks(team_dict)
    team_dict = calculate_western_adjustment(isr_dict, team_dict)
    print(f"After Western Adjustment: {team_dict['STANFORD']['adjusted_rpi']}")
    team_dict = calculate_conf_adjustment(team_dict)
    print(f"After Conference Adjustment: {team_dict['STANFORD']['adjusted_rpi']}")
    team_dict = calculate_group_adjustments(team_dict)
    print(f"After Group Adjustment: {team_dict['STANFORD']['adjusted_rpi']}")
    team_dict = set_auto_bids(auto_bids, team_dict)
    create_tourney_ranks(team_dict)


if __name__ == '__main__':
    main()







