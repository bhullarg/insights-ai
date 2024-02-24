import argparse
import os
import exp_configs
import shutil

from src import utils as ut



def main(exp_dict, savedir, args):
    """
    main function for running experiments
    -  exp_dict: dictionary of hyperparameters
    -  savedir: directory to save results
    -  args: additional arguments
    """
    # Print Experiment
    print(f"\nRunning experiment with hyperparameters:\n{exp_dict}\n")

    if args.reset:
        # delete folder if it exists
        if os.path.exists(savedir):
            shutil.rmtree(savedir)

    # create folder
    os.makedirs(savedir, exist_ok=True)

    # Load Data
    if exp_dict["data"] == "quantum_physics":
        data = ut.read_text(os.path.join("data", "quantum_physics.txt"))

    # Run Method & Get Output
    if exp_dict["method"] == "base":
        summary = ut.get_summary(data)

    # Print & Save Output
    print(summary)
    ut.save_summary(savedir, summary)

    print("\nExperiment Completed and Saved in ", savedir)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Read and summarize a text file.")
    # add exp_group
    parser.add_argument("-e", "--exp_group", default="base", help="Experiment group")
    # add reset as int
    parser.add_argument("-r", "--reset", default=1, help="Reset the savedir")
    args = parser.parse_args()
    
    # Loop through experiments
    for exp_dict in exp_configs.EXP_GROUPS[args.exp_group]:
        # savedir
        hparam = '_'.join([f"{value}" for key, value in sorted(exp_dict.items())])
        savedir = os.path.join("results", hparam)

        # run main
        main(exp_dict, savedir, args)
    