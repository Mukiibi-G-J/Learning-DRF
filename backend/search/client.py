from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


def get_index(index_name="jeff_Product"):
    #cfe_Article
    client = get_client()

    index = client.init_index(index_name)

    return index


# perform_search("hello", tags=["electronics"], public=True)


def perform_search(query, **kwargs):
    index = get_index()
    tags = ""
    params = {}
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []

        if len(tags) != 0:
            params["tagFilters"] = tags
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]
    if len(index_filters) != 0:
        params["facetFilters"] = index_filters
    results = index.search(query, params)

    return results
