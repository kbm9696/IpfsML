import store_data_sets


if __name__ == '__main__':
    print('in testing face')
    # t = store_data_sets.upload_dataset('polygon','polygon_wallet.csv')
    # t = store_data_sets.get_dataset('polygon')
    # t = store_data_sets.upload_model('polygon1', 'polygon_wallet.h5')
    t = store_data_sets.get_model('polygon')
    print('ahah',t)
