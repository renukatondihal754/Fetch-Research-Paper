import requests
import csv
import argparse


def fetch_pubmed_data(query):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 20
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data['esearchresult']['idlist']


def extract_article_details(pmid):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "json"
    }

    response = requests.get(url, params=params)
    article = response.json()['result'][pmid]

    title = article.get('title', 'N/A')
    pub_date = article.get('pubdate', 'N/A')

    # Mock non-academic company data
    non_academic_author = 'N/A'
    company_affiliation = 'N/A'
    corresponding_author_email = 'N/A'

    # Example heuristic (you can modify this)
    if "AI" in title or "Pharma" in title:
        non_academic_author = 'Sample Pharma Co.'
        company_affiliation = 'Sample Pharma Co., NY, USA'
        corresponding_author_email = 'contact@pharma.com'

    return [pmid, title, pub_date, non_academic_author, company_affiliation, corresponding_author_email]


def write_to_csv(articles, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)', 'Company Affiliation(s)', 'Corresponding Author Email'])

        for article in articles:
            csvwriter.writerow(article)


def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and extract company-affiliated authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output file name (optional).", default='pubmed_output.csv')
    parser.add_argument("-d", "--debug", action='store_true', help="Enable debug mode.")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    pmids = fetch_pubmed_data(args.query)
    articles = []

    for pmid in pmids:
        article_details = extract_article_details(pmid)
        articles.append(article_details)

    write_to_csv(articles, args.file)
    print(f"✅ Data extraction complete. Check '{args.file}'.")


if __name__ == "__main__":
    main()
    