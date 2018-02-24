#----------------------------------------------------
# Name: Manjun Lu

# Assignment: DNS Server Project

# Reference:
#    https://en.wikipedia.org/wiki/List_of_DNS_record_types
#    http://www.dnspython.org/examples.html


import sys
import dns.resolver

def main():
    if(len(sys.argv) != 3 ):
        print('You enter the wrong command')
    else:
        print("Please enter a domian name and type one option from --AAAA/--MX/--A")

        program_name = sys.argv[0]
        domainName = sys.argv[1]
        action = sys.argv[2]

    #print(domainName)
    #print(action)
    # assert action in ['--AAAA','--MX', '--APL']
        if( action in ['--AAAA','--MX', '--A']):
        #for a in action:
            process(domainName,action)
        else:
            print('Please reselect command')


def process(domainName, action): 
    print(action)
    if action == '--AAAA':
        #print('string')
        answers = dns.resolver.query(domainName, 'AAAA')
        for i in answers:
            print(i)

    elif action == '--MX':
        answers = dns.resolver.query(domainName, 'MX')
        for i in answers:
            print(i)
    elif action == '--A':
        answers = dns.resolver.query(domainName, 'A')
        for i in answers:
            print(i)


if __name__ == "__main__":
    # calling the main function
    main()