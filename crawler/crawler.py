
import crawler

fetcher = crawler.ArticleFetcher()
counter= 0
for element in fetcher.fetch():
    print(element.title + element.emoji)
    counter +=1
    if counter == 9:
        break


