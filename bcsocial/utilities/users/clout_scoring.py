# Users clout scoring based on users interactions with different questions and how other users engage with their comments. Current hard coded values are for testing purposes only.

user_cat = 4
total_cat = 5
user_votes = 0
available_votes = user_cat * 100
user_comments = 0
user_agreements = 421

def user_cat_score():
  return round(user_cat / total_cat * 100)

def user_vote_score():
    #additional logic will be needed to limit the number of votes counted to fall within the last 30 days
    if user_votes > available_votes:
        raise ValueError('user votes cannot be greater than available votes')
    if user_votes != 0:
        return round((user_votes / available_votes) * 100, 2)
    else:
        return "user has not voted"

def user_pop_score():
    #additional logic will be needed to limit the number of comments and agreements counted to fall within the last 90 days
    if user_comments == 0:
        user_agreements = 0
        return "no comments to calculate"
    return round((user_agreements / user_comments) * 100, 2)

print(user_cat_score())
print(user_vote_score())
print(user_pop_score())