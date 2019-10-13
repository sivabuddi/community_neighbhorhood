from google_images_download import google_images_download

google = google_images_download.googleimagesdownload()
# result = google ._get_all_items('https://www.google.com/search?q=abandoned+house&rlz=1C1CHBF_enUS811US811&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjvmfyO4K3kAhUIv54KHVM_BuYQ_AUIESgB&biw=1536&bih=722', 'WebScraping',
#                                 'images', 100, )
# print(result)

args_list = ["keywords_from_file", "prefix_keywords", "suffix_keywords",
             "limit", "format", "color", "color_type", "usage_rights", "size",
             "exact_size", "aspect_ratio", "type", "time", "time_range", "delay", "url", "single_image",
             "output_directory", "image_directory", "no_directory", "proxy", "similar_images", "specific_site",
             "print_urls", "print_size", "print_paths", "metadata", "extract_metadata", "socket_timeout",
             "thumbnail", "thumbnail_only", "language", "prefix", "chromedriver", "related_images", "safe_search", "no_numbering",
             "offset", "no_download","save_source","silent_mode","ignore_urls"]

#Google abandoned houses
#page = google.download_page('https://www.google.com/search?q=abandoned+house&rlz=1C1CHBF_enUS811US811&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjvmfyO4K3kAhUIv54KHVM_BuYQ_AUIESgB&biw=1536&bih=722')

#Kansas city rent link
page = google.download_page('https://www.google.com/search?biw=1853&bih=981&tbm=isch&sxsrf=ACYBGNTNIs0O35wgERGk7ZyDoyy-QsGB2Q%3A1570934662714&sa=1&ei=ho-iXeKKK4KosgXY2q2oDw&q=rainbow+houses+lbgtq+usa+outside+houses&oq=rainbow+houses+lbgtq+usa+outside+houses&gs_l=img.3...17887.19369..20227...0.0..0.101.580.4j2......0....1..gws-wiz-img.GfglOFNwWQk&ved=0ahUKEwji5aTUm5jlAhUClKwKHVhtC_UQ4dUDCAc&uact=5')

data = google._get_next_item(page)
argumnets = {
        "keywords": "house",
        "limit": 5,
        "print_urls": False,
        "image_directory":'images',
        "offset":False,
        "metadata": True,
        "silent_mode":True,
        "socket_timeout": False,
        "prefix": 'house',
        "print_size":True,
        "no_numbering":False,
        "no_download": False,
        "save_source": True,
        "thumbnail_only": False,
        "format": True,
        "size":'>800*600',
    "exact_size": True,
    "exact_size": "1024,768"

}

for item in args_list:
    if item in ["output_directory","image_directory","no_directory","thumbnail","keywords", "limit","no_numbering", "size", "exact_size"]:
        argumnets[item] = True
    else:
        argumnets[item] = False
print(argumnets)
google._get_all_items(page, 'kansas city','images', 400, argumnets)
