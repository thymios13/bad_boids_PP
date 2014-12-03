# PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH python record_fixture.py
import yaml
import boids
from copy import deepcopy
before = deepcopy(boids.boids)
boids.update_boids(boids.boids)
after = boids.boids
before = tuple(map(list, before))
after = tuple(map(list, after))
print before
print "----------"
print after

fixture = {"before": before, "after": after}
print fixture
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()