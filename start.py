import matches
import score
import time

matches.show_current()

match = int(input("Enter the number of the match: "))

global link_match
url = "https://www.cricbuzz.com" + matches.link_match[match-1]


while True:
    try:
        score.get_score(url)
        for it in range(5):
                time.sleep(1)

    except KeyboardInterrupt:
        import sys
        sys.exit()
