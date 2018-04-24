from pomegranate import *

a = DiscreteDistribution( { '0':0.5, '1':0.5 } )
p = DiscreteDistribution( { '0':0.5, '1':0.5 } )

g = ConditionalProbabilityTable(
        [[ '0', '0', 0.3 ],
         [ '0', '1', 0.7 ],
         [ '1', '0', 0.6 ],
         [ '1', '1', 0.4 ]],
         [a] )

i = ConditionalProbabilityTable(
        [[ '0', '0', 0.25 ],
         [ '0', '1', 0.75 ],
         [ '1', '0', 0.20 ],
         [ '1', '1', 0.80 ]],
         [p] )

d = ConditionalProbabilityTable(
        [[ '0', '0', '0', 0.45 ],
         [ '0', '1', '0', 0.75 ],
         [ '1', '0', '0', 0.30 ],
         [ '1', '1', '0', 0.15 ],
         [ '0', '0', '1', 0.55 ],
         [ '0', '1', '1', 0.25 ],
         [ '1', '0', '1', 0.70 ],
         [ '1', '1', '1', 0.85 ]],
         [p, a] )

v = ConditionalProbabilityTable(
        [[ '0', '0', '0', 0.3 ],
         [ '0', '1', '0', 0.5 ],
         [ '1', '0', '0', 0.8 ],
         [ '1', '1', '0', 0.6 ],
         [ '0', '0', '1', 0.7 ],
         [ '0', '1', '1', 0.5 ],
         [ '1', '0', '1', 0.2 ],
         [ '1', '1', '1', 0.4 ]],
         [g, i] )

s_a = State( a, name="A" )
s_p = State( p, name="P" )
s_i = State( i, name="I" )
s_g = State( g, name="G" )
s_d = State( d, name="D" )
s_v = State( v, name="V" )

model = BayesianNetwork("Elections")

model.add_states(s_a, s_p, s_i, s_g, s_d, s_v)

model.add_transition(s_g, s_v)
model.add_transition(s_i, s_v)
model.add_transition(s_p, s_i)
model.add_transition(s_p, s_d)
model.add_transition(s_a, s_g)
model.add_transition(s_a, s_d)

model.bake()

v_distribution = model.predict_proba({})[-1]
v_probabilities = v_distribution.parameters[0]

print(v_probabilities['1'])
# 1) My oponent is charted to win the congressional seat
print(v_probabilities['0'] - v_probabilities['1'] )
# by a margin of ~12%

print('\nPart 2\n')

'''
Second, for each of the following,
(a) compute the probability requested and then
(b) determine if should target the individual for canvassing (when oponent wins '0' > '1')
(c) record their values in your report.
'''
# oponent wins -> target
v_distribution = model.predict_proba({'A':'1'})[-1]
v_probabilities = v_distribution.parameters[0]
print(v_probabilities)

# I win -> DONT target
v_distribution = model.predict_proba({'G':'0'})[-1]
v_probabilities = v_distribution.parameters[0]
print(v_probabilities)

# I win -> DONT target
v_distribution = model.predict_proba({'G':'0','I':'0'})[-1]
v_probabilities = v_distribution.parameters[0]
print(v_probabilities)

# oponent wins -> target
v_distribution = model.predict_proba({'I':'0','G':'1'})[-1]
v_probabilities = v_distribution.parameters[0]
print(v_probabilities)

# I win -> DONT target
v_distribution = model.predict_proba({'A':'0','P':'1','I':'0','D':'0','G':'0'})[-1]
v_probabilities = v_distribution.parameters[0]
print(v_probabilities)

# I ALMOST WIN -> target
v_distribution = model.predict_proba({'A':'0','P':'1','I':'1','D':'1','G':'0'})[-1]
v_probabilities = v_distribution.parameters[0]
print(v_probabilities)

# oponent wins -> target
v_distribution = model.predict_proba({'A':'1','P':'0','I':'0','D':'0','G':'1'})[-1]
v_probabilities = v_distribution.parameters[0]
print(v_probabilities)

'''
RESULTS FOR BN:

{'0': 0.5309999999999999, '1': 0.469}
{'0': 0.455, '1': 0.545}
{'0': 0.3000000000000001, '1': 0.6999999999999998}
{'0': 0.7999999999999999, '1': 0.20000000000000015}
{'0': 0.3000000000000001, '1': 0.6999999999999998} 1
{'0': 0.5, '1': 0.5}                               0
{'0': 0.7999999999999999, '1': 0.20000000000000015}0

'''
