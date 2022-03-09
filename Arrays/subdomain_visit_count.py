import collections


def cound_visit_subdomain(cpdomains):
  ans = collections.defaultdict(int)

  for domain in cpdomains:
    count, domain = domain.split()
    count = int(count)
    subdomains = domain.split(".")

    for i in range(len(subdomains)):
      ans[".".join(subdomains[i:])] += count

  return ['{} {}'.format(v,k) for k, v in ans.items()]

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(cound_visit_subdomain(cpdomains))

