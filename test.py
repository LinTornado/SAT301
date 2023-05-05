# from bert_score import score
#
# print(score(['i have a apple'], ['the apple'],lang='en',verbose=True))

import bert_score
from bert_score import score
from rouge import Rouge

# Read the content of the file and remove blank lines
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # lines = [line.strip() for line in lines if line.strip()]
    return lines


# Read reference summary and generate summary
ref_summaries = read_file("giga_word/test/title_filtered.txt")
gen_summaries = read_file("result.txt")

# Initialize Rouge Object
rouge = Rouge()

# Initialize the total Rouge-1, Rouge-2, and Rouge-L indicators
rouge_1_total = 0
rouge_2_total = 0
rouge_l_total = 0

# Recursively calculate the Rouge-1,2,L indicates for each generated summary and corresponding reference summary,
# and calculate the total Rouge-1,2,L indicates
for i, gen_summ in enumerate(gen_summaries):

    # Skip this loop if the generated summary is empty
    if not gen_summ:
        continue

    ref_summ = ref_summaries[i]
    scores = rouge.get_scores(gen_summ, ref_summ)
    rouge_1 = scores[0]['rouge-1']['f']
    rouge_1_total += rouge_1
    rouge_2 = scores[0]['rouge-2']['f']
    rouge_2_total += rouge_2
    rouge_l = scores[0]['rouge-l']['f']
    rouge_l_total += rouge_l
    #print(i)
    #print(scores)


# Calculate the average Rouge-1,2,L indicator
rouge_1_avg = rouge_1_total / len(gen_summaries)
rouge_2_avg = rouge_2_total / len(gen_summaries)
rouge_l_avg = rouge_l_total / len(gen_summaries)

print("Average Rouge-1 Indicator: {:.4f}".format(rouge_1_avg))
print("Average Rouge-2 Indicator: {:.4f}".format(rouge_2_avg))
print("Average Rouge-l Indicator: {:.4f}".format(rouge_l_avg))

# Calculate BertScore separately for each row
P, R, F1 = bert_score.score(gen_summaries, ref_summaries, lang="en")

# Calculate the average BertScore metric for all reference summary and generated summary
avg_P = sum(P) / len(P)
avg_R = sum(R) / len(R)
avg_F1 = sum(F1) / len(F1)

# print(len(P))
# print(R)
# print(F1)
print("Average BertScore Indicator：Precision={:.4f}, Recall={:.4f}, F1={:.4f}".format(avg_P, avg_R, avg_F1))