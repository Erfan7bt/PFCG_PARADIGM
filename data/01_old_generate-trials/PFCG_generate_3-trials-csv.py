import pandas as pd
import numpy as np

def generate_new_master(n_blocks=10, trials_per_cue=3, cues_per_block=20):
    data = []
    
    for block in range(1, n_blocks + 1):
        # We want an equal mix of congruent (1) and incongruent (0) cues
        cues = [0, 1] * (cues_per_block // 2)
        np.random.shuffle(cues)
        
        for cue in cues:
            cue_str = "cong" if cue == 1 else "incg"
            
            # For each cue, generate 3 trials
            # We want to randomize trial types (left/right) within these 3 trials
            # trialtype: 0=right_cong, 1=left_cong, 2=right_incg, 3=left_incg
            for _ in range(trials_per_cue):
                if cue == 1: # Congruent
                    ttype = np.random.choice([0, 1])
                    ttype_str = "right_cong" if ttype == 0 else "left_cong"
                    ckey = "right" if ttype == 0 else "left"
                else: # Incongruent
                    ttype = np.random.choice([2, 3])
                    ttype_str = "right_incg" if ttype == 2 else "left_incg"
                    ckey = "left" if ttype == 2 else "right" # Incongruent keys are flipped
                
                data.append([block, cue, cue_str, ttype, ttype_str, ckey])

    df = pd.DataFrame(data, columns=['block', 'cuetype', 'cuetype_string', 'trialtype', 'trialtype_string', 'correct_key'])
    df.to_csv("master_blocks.csv", index=False)
    print("New master_blocks.csv with 3 trials per cue created.")

generate_new_master()