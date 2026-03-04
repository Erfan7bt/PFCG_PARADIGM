import pandas as pd
import numpy as np

# --- SETTINGS: Change these numbers as needed ---
TRIALS_PER_CUE = 4   # Set this to 3, 4, 5, etc.
N_BLOCKS = 10
CUES_PER_BLOCK = 20
# -----------------------------------------------



def generate_new_master(blocks, trials, cues):
    data = []
    
    for block in range(1, blocks + 1):
        # Create an equal mix of congruent (1) and incongruent (0) cues
        cue_list = [0, 1] * (cues // 2)
        np.random.shuffle(cue_list)
        
        for cue in cue_list:
            cue_str = "cong" if cue == 1 else "incg"
            
            # Generate the specified number of trials for this cue
            for _ in range(trials):
                if cue == 1: # Congruent logic
                    ttype = np.random.choice([0, 1])
                    ttype_str = "right_cong" if ttype == 0 else "left_cong"
                    ckey = "right" if ttype == 0 else "left"
                else: # Incongruent logic
                    ttype = np.random.choice([2, 3])
                    ttype_str = "right_incg" if ttype == 2 else "left_incg"
                    ckey = "left" if ttype == 2 else "right" # Keys are flipped
                
                data.append([block, cue, cue_str, ttype, ttype_str, ckey])

    df = pd.DataFrame(data, columns=['block', 'cuetype', 'cuetype_string', 'trialtype', 'trialtype_string', 'correct_key'])
    df.to_csv("master_blocks.csv", index=False)
    print(f"Successfully created master_blocks.csv with {trials} trials per cue.")
    print(f"Total rows: {len(df)} (plus header)")

# Run the function using the variables from the top
generate_new_master(N_BLOCKS, TRIALS_PER_CUE, CUES_PER_BLOCK)