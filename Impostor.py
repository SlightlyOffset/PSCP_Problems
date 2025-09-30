'''Impostor'''
import re
def main():
    '''main'''
    # init empty dict to store crew members
    # init lines to temporary store inputs
    crew = {}
    lines = []

    # add crew members till input is 'Start'
    add_crew = True
    while add_crew:
        line = input().strip()
        if line == 'Start':
            add_crew = False
            continue
        lines.append(line)

    # 3val all crew input(confirm dict-like structure) and add to master dict(crew)
    for line in lines:
        match = re.match(r'\{"(.+?)"\s*:\s*"(.+?)"}', line)
        if match:
            name, role = match.groups()
            crew[name] = role


    # init dead and alive dict
    alive = crew.copy()
    dead = {}

    # vote out crew members
    # delete from alive and add to dead
    vote_out = True
    while vote_out:
        vote = input().strip()
        if vote == 'End':
            vote_out = False
            continue
        alive.pop(vote)
        dead.update({vote: crew[vote]})

    # sort alive and dead dict character wise
    alive = dict(sorted(alive.items()))
    dead = dict(sorted(dead.items()))


    # count for remaining impostor
    imposter_remain = 0
    for role in alive.values():
        if role == 'Impostor':
            imposter_remain += 1


    # begin print out results
    print(f"{imposter_remain} Impostor Remains")
    print("***Alive***")
    for member, role in alive.items():
        print(f"{member} : {role}")
    print("***Dead***")
    for member, role in dead.items():
        print(f"{member} : {role}")

if __name__ == '__main__':
    main()
