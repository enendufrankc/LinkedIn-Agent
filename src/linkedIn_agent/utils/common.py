from bs4 import BeautifulSoup


def parse_html_content(page_source: str):
    """
    Parses the page source HTML of a LinkedIn profile and filters 
    the containers that contain post information.
    """
    linkedin_soup = BeautifulSoup(page_source.encode("utf-8"), "lxml")
    containers = linkedin_soup.find_all("div", {"class": "feed-shared-update-v2"})
    containers = [container for container in containers 
                  if 'activity' in container.get('data-urn', '')]
    return containers

def get_post_content(container, selector, attributes):
    """
    Retrieves the text content from a specific HTML element 
    within a container.
    """
    try:
        element = container.find(selector, attributes)
        if element:
            return element.text.strip()
    except Exception as e:
        print(f"Error extracting post content: {e}")
    return ""

def get_linkedin_posts(page_source: str):
    """
    Uses parse_html_content to identify relevant containers, then 
    extracts the post text from each container.
    """
    containers = parse_html_content(page_source)
    posts = []
    for container in containers:
        post_content = get_post_content(container, "div", {"class": "update-components-text"})
        posts.append(post_content)
    return posts
