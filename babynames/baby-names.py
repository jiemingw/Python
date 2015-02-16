__author__ = 'jiemingw'
import sys
import re

def extract_names(filename):
  names_list=[]

  f = open(filename, 'rU')
  text_all = f.read()

  year = re.search(r'Popularity\sin\s(\d\d\d\d)', text_all)
  if year:
      names_list.append(year.group(1))
  else:
      return 'match not found'
#      sys.stderr.write('Couldn\'t find the year!\n')
#      sys.exit(1)

  baby_names_tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text_all)

  names_to_rank =  {}
  if baby_names_tuples:
      for tuple in baby_names_tuples:
          (rank, name_boy, name_girl) = tuple
          if name_boy not in names_to_rank:
            names_to_rank[name_boy] = rank
          if name_girl not in names_to_rank:
            names_to_rank[name_girl] = rank
      sorted_names = sorted(names_to_rank.keys())
      for name in sorted_names:
          names_list.append(name + " " + names_to_rank[name])
  else:
      return 'match not found'

  return names_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
    names = extract_names(filename)
    names_str = '\n'.join(names)

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(names_str + '\n')
      outf.close()
    else:
      print names

if __name__ == '__main__':
  main()