import pandas as pd
import json

# Load JSON file
with open('concepts.json', 'r') as json_file:
    data = json.load(json_file)

# Flatten the JSON structure
flattened_data = []
for entry in data:
    concept = entry['concept']
    implementation = entry['implementation']
    explanation = entry['explanation']
    asset_suggestions = entry['asset_suggestions']

    for suggestion in asset_suggestions:
        frame_1 = suggestion['frame_1']
        frame_2 = suggestion['frame_2']
        frame_3 = suggestion['frame_3']
        suggestion_explanation = suggestion['explanation']

        flattened_entry = {
            'concept': concept,
            'implementation_frame_1': list(implementation.values())[0],
            'implementation_frame_2': list(implementation.values())[1],
            'implementation_frame_3': list(implementation.values())[2],
            'frame_1': frame_1,
            'frame_2': frame_2,
            'frame_3': frame_3,
            'explanation': explanation,
            'suggestion_explanation': suggestion_explanation
        }
        flattened_data.append(flattened_entry)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

# Display the DataFrame
print(df)