

def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    if final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    if final_score["home_score"] == final_score["away_score"]:
        return "Draw"



def get_results(final_scores):
    result_list = []
    for score in final_scores: 
        result_list.append(get_result(score))
    return result_list


    #     if score["home_score"] > score["away_score"]:
    #         result_list.append("Home win")
    #     if score["home_score"] < score["away_score"]:
    #         result_list.append("Away win")
    #     if score["home_score"] == score["away_score"]:
    #         result_list.append("Draw")

    # return result_list