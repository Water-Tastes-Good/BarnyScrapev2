# append site to site_input_here.txt via sets

# no repeating values 

# display titles & allow editing of titles

# begin tiktokpassivedatafetch.py program w/
# valid inputs

# have display showing list of unuploaded links
# w/ number count 

# seperate button to start BarnyScrape


# show status of upload 

# Future:
# add emojis on random basis to titles

class links:
    def __init__(self):
        MAIN_INPUT_FILE = 'site_input_here.txt'
        LINK_SET = {}

    def append_to_link_set(self, link_to_append):
        LINK_SET = LINK_SET.append(link_to_append)
        
    def write_to_file(self):
        with open('site_input_here.txt', 'w') as link_list:
            # send notification to user their inputs will be cleared
            # write LINK_SET to MAIN_INPUT_FILE
            link_list.write(LINK_SET)
        return 'WRITTEN!'

create = links.append_to_link_set(link_to_append)