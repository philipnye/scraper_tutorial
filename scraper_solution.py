# %%
import requests
from bs4 import BeautifulSoup

# %%
# Define a list of primary free school URNs
target_urns = [
    136807, 136808, 136821, 136930, 136934, 136938, 136951, 136952, 137016, 137281,
    137320, 137323, 137324, 137326, 137331, 137488, 137492, 138201, 138203, 138231,
    138232, 138252, 138257, 138258, 138259, 138261, 138263, 138268, 138270, 138272
]

# %%
# Iterate over URNs, printing URN + inspection rating where one
# can be found
for target_urn in target_urns:
    target_url = 'https://reports.ofsted.gov.uk/provider/21/' + str(target_urn)

    r = requests.get(target_url)
    soup = BeautifulSoup(r.content, features='html.parser')

    if soup.find("h2", class_="latest-rating__title") is None:
        print(target_urn, "No rating found", sep=" ")
    else:
        print(
            str(target_urn),
            soup.find("h2", class_="latest-rating__title").span.contents[0],
            sep=" "
        )

# %%
