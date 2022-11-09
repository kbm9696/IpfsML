from IpfsML import store_data_sets


if __name__ == '__main__':
    print('in testing face')
    #t = store_data_sets.upload_dataset('chicken_derby','datasets/chicken_nft_.csv')
    t = store_data_sets.search('polygonv')
    # t = store_data_sets.upload_model('polygon1', 'polygon_wallet.h5')
    #t = store_data_sets.get_model('polygon')
    print('ahah',t)
