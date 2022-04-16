import sys


def start():
    argv = sys.argv[1:]
    pt = False

    use = [x for x in argv if x.__contains__('/') or x.__contains__('--')]
    use.extend([x for x in argv if x=='-a' or x=='-m' or x=='-h' or x=='-e'])

    for u in use:
        argv.remove(u)
    
    argv = [float(x) for x in argv]
    printing = ['/e', '/expression', '-e', '--expression']
    adding = ['/a', '/add', '-a', '-add']
    prod = ['/m', '/mul', '-m', '--mul']
    help = ['-h', '--help', '/?']
    
    for u in use:
        if printing.__contains__(u):
            pt = True
            break

    for u in use:
        if adding.__contains__(u):
            sums(argv, pt)
        elif prod.__contains__(u):
            iloczyn(argv, pt)
        elif help.__contains__(u):
            help_mess()
        else:
            help_mess()


def sums(args, pt):
    s=0
    for arg in args:
        s += arg

    if not pt:
        print(s)
    else:
        m = ''
        l = len(args)
        for i in range(l):
            m += str(args[i])
            if i != l-1:
                m += ' + '
            else:
                m += ' = ' + str(s)
        print(m)

def iloczyn(args, pt):
    p = 1
    for arg in args:
        p *= arg

    if not pt:
        print(p)
    else:
        m = ''
        l = len(args)
        for i in range(l):
            m += str(args[i])
            if i != l-1:
                m +=' * '
            else:
                m += ' = '+str(p)
        print(m)


def help_mess():
    print('help')

start()