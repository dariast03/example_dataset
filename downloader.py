# from bing_image_downloader import downloader
# downloader.download("chacarera tarija vestimenta", limit=100,  output_dir='data_downloader', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

import simple_image_download.simple_image_download as simp


my_downloader = simp.Downloader()
#my_downloader.search_urls('Landsapes',limit=10, verbose=True)

# Get List of Saved URLs in cache
#print(my_downloader.get_urls())

# Prints the Whole Cache
#print(my_downloader.cached_urls)

# Download + search file
#my_downloader.download('spaceship', limit=2)

# Now donwload all the Searched picture
#my_downloader.download(download_cache=True)

# Flush cache
#my_downloader.flush_cache()

# Change Direcotory
my_downloader.directory = 'data_downloader/'
# Change File extension type
#my_downloader.extensions = '.jpg'
#print(my_downloader.extensions)
my_downloader.download('potolos vestimenta', limit=100, num_pages=1, verbose=True)
