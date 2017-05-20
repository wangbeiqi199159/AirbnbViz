def generate_ranked_data():
    data1 = pd.read_csv("../../data/listings.csv")
    data2 = pd.read_csv("../../data/listings2.csv")
    neighbourhood = data1['neighbourhood_group'].tolist()
    price = data1['price'].tolist()
    rating = data2['review_scores_rating'].tolist()

    # neighbourhood name list
    name_list = [data1['neighbourhood_group'][0]]
    n = len(neighbourhood)
    for i in range(1, n):
        if neighbourhood[i] != neighbourhood[i - 1]:
            name_list.append(neighbourhood[i])

    # avg price, avg rating by neighbourhood
    price_list = data1.groupby(data1.neighbourhood_group).mean()['price']
    rating_list = data2.groupby(data1.neighbourhood_group).mean()['review_scores_rating']

    avg_price = []
    avg_rating = []

    d = len(name_list)
    for i in range(0, d):
        price_target = price_list[name_list[i]]
        rating_target = rating_list[name_list[i]]
        avg_price.append(price_target)
        avg_rating.append(rating_target)

    # generate ranked price js file
    ranked_price_list = price_list.sort_values(ascending=False)
    ranked_price_index = ranked_price_list.index.tolist()
    ranked_price_value = ranked_price_list.tolist()

    df_price = pd.DataFrame({'ranked_price_index': ranked_price_index, 'ranked_price': ranked_price_value})
    df_price = df_price.to_json(orient='records')

    price_filepath = "../../js/ranked_price_data_by_group.js"
    price_file = open(price_filepath, "w")
    price_file.write("var ranked_price_data_by_group = " + df_price);
    price_file.close()

    # generate ranked rating js file
    ranked_rating_list = rating_list.sort_values(ascending=False)
    ranked_rating_index = ranked_rating_list.index.tolist()
    ranked_rating_value = ranked_rating_list.tolist()

    df_rating = pd.DataFrame({'ranked_price_index': ranked_rating_index, 'ranked_price': ranked_rating_value})
    df_rating = df_rating.to_json(orient='records')

    rating_filepath = "../../js/ranked_rating_data_by_group.js"
    rating_file = open(rating_filepath, "w")
    rating_file.write("var ranked_rating_data_by_group = " + df_rating);
    rating_file.close()
