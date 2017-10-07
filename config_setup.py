import string
import time

def setup(container, config):
	# setting up variables using config file
	for rules in config:
		# split the rules into words
		info = rules.split(" ")

		if info[0] == "mu:":
			container.populationSize = info[1]
		elif info[0] == "lambda:":
			container.offspringSize = info[1]
		elif info[0] == "runs:":
			container.numRuns = info[1]
		elif info[0] == "newSeed":
			if info[2] == '1':
				for rules in config:
					info = rules.split(" ")
					if info[0] == "seed:":
						container.seed = eval(info[1])
						break
			else:
				obtain_seed = open(container.prob_log_file).read().splitlines(3)
				for lines in obtain_seed:
					line = lines.split(" ")
					if line[0] == "Random":
						container.seed = line[3]
						break
		elif info[0] == "mutation_rate:":
			container.mutationRate = info[1]
		elif info[0] == "fitness_evaluations:":
			container.evaluations = info[1]
		elif info[0] == "prob_log:":
			container.prob_log_file = info[1]
		elif info[0] == "number_of_evals_till_termination:":
			container.numEvalsTerminate = info[1]
		elif info[0] == "tournament_size_for_parent_selection:":
			container.kParent = info[1]
		elif info[0] == "tournament_size_for_survival_selection:":
			container.kOffspring = info[1]
		elif info[0] == "n_for_termination_convergence_criterion:":
			container.n = info[1]
		elif info[0] == "prob_solution:":
			container.prob_solution_file = info[1]
		elif info[0] == "Initialization:":
			if info[1] == "Uniform_Random:" and info[2] == '1':
				# sets flag for uniform random
				container.uniformRandom = 1
		elif info[0] == "Parent_Selection:":
			if info[1] == "Fitness_Proportional_Selection:" and info[2] == '1,':
				# sets flag for fitness selection
				container.fitnessSelection = 1
			elif info[3] == "k-Tournament_Selection_with_replacement:" and info[4] == '1':
				# sets flag for parent tournament
				container.parentTournament = 1
		elif info[0] == "Survival_Selection:":
			if info[1] == "Truncation:" and info[2] == '1,':
				container.truncation = 1
			elif info[3] == "k-Tournament_Selection_without_replacement:" and info[4] == '1':
				container.offspringTournament = 1
		elif info[0] == "Termination:":
			if info[1] == "Number_of_evals:" and info[2] == '1,':
				container.numEvals = 1
			elif info[3] == "no_change_in_average_population_fitness_for_n_generations:" and info[4] == '1,':
				# sets flag for parent tournament
				container.avgPopFitness = 1
			elif info[5] == "no_change_in_best_fitness_in_population_for_n_generations:" and info[6] == '1':
				# sets flag for parent tournament
				container.bestPopFitness = 1