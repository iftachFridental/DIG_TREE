import dns.resolver
import tldextract 

DNS_RESOLVER = dns.resolver.Resolver()


def get_domain_from_url(url: str) -> str:
    """ return normalized domain from url """
    parsed_url = tldextract.extract(url)
    return f"{parsed_url.domain}.{parsed_url.suffix}"


def get_nameservers(domain: str) -> list:
    """ Request a NS query for the domain and returns the NS servers as a list """
    servers_arr = []
    for server in DNS_RESOLVER.query(domain, 'NS'):
        servers_arr.append(get_domain_from_url(str(server.target)))
    return list(set(servers_arr))
