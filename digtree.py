import sys
import resolver
import treeprinter
import argparse



def get_dependencies_db(domain: str) -> dict:
	""" creates a printable db for the domain NS dependencies """

	domains_to_handle = []
	domains_to_handle.append(domain)

	printable_dependencies_db = {}

	while len(domains_to_handle) > 0:
	    current_domain = domains_to_handle.pop()

	    printable_dependencies_db[current_domain] = {'children': [], 'color': 'green'} # initialized as in-bailiwick

	    for server in resolver.get_nameservers(current_domain):
	        if server not in printable_dependencies_db:
	            domains_to_handle.append(server)

	        if server != current_domain:
	            printable_dependencies_db[current_domain]['children'].append(server)
	            printable_dependencies_db[current_domain]['color'] = 'red' # out-of-bailiwick
	
	return printable_dependencies_db


def main():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("domain", help="the domain which you want to find his NS dependencies")
	user_args = arg_parser.parse_args()

	normalized_domain = resolver.get_domain_from_url(user_args.domain)
	treeprinter.print_tree(get_dependencies_db(normalized_domain), normalized_domain)


if __name__ == '__main__':
	main()
