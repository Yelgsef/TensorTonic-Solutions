def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    ans = []
    stop_set = set(stopwords)
    for token in tokens: 
        if (token not in stop_set):
            ans.append(token)
    return ans 
    pass