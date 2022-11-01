import totoScraper
import unibetScraper
import merger
import arbitrage_calculator

if __name__ == "__main__":
    toto = totoScraper.main()
    unibet = unibetScraper.main()
    scrapes = [toto, unibet]
    merged = merger.merge(scrapes)
    arbitrage_calculator.calculate(merged)
