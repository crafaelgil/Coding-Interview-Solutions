import collections

def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
  subdomains_map = collections.defaultdict(int)

  for domain in cpdomains:
      count, domains = domain.split()
      count = int(count)
      subdomains = domains.split(".")
      for i in range(len(subdomains)):
          subdomains_map[".".join(subdomains[i:])] += count

  return ['{} {}'.format(value, key) for key, value in subdomains_map.items()]
