import totoScraper
import unibetScraper
import merger

if __name__ == "__main__":
    toto = totoScraper.main()
    unibet = unibetScraper.main()
    scrapes = [toto, unibet]
    merger.merge(scrapes)
