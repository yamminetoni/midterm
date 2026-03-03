def is_valid_url(url):
    # check type
    if type(url) != str:
        return False

    # check starting part
    if url.startswith("http://") or url.startswith("https://"):

        # check no spaces
        if " " in url:
            return False

        # check if there is a dot after the protocol
        if "." in url:
            if len(url) > 8:
                return True

    return False