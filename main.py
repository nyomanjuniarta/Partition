import sys
from CSCPattern import Pattern, PatternConfig
from diagram import init_diagram, add_intent, add_object, clean_flags, print_lattice

if __name__ == "__main__":
    path = sys.argv[1]
    if len(sys.argv) > 2:
        theta = int(sys.argv[2])
    else:
        theta = 1
    cfg = PatternConfig(theta)
    with open(path, 'r') as f:
        L = init_diagram()
        #print_lattice(L, path + '_lattice.txt')
        print L.node[-1]
        for object_id, line in enumerate(f):
            raw_entry = line.replace('\n', '').replace('\r', '')
            pattern = Pattern(instance=raw_entry, config=cfg, object=object_id)
            print '\npartitions ', pattern
            object_concept_id = add_intent(pattern, -1, L, 0)
            add_object(object_concept_id, object_id, L)
            clean_flags(L, object_concept_id)
    L = L.reverse()
    print_lattice(L, path + '_lattice.txt')