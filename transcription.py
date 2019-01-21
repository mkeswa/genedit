import difflib
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/diff")
def hello():
    return jsonify(diff(read_sequence_file(request.args.get("first_sequence")), read_sequence_file(request.args.get("second_sequence"))))


def diff(sequence1, sequence2):
    d = difflib.SequenceMatcher(None, sequence2, sequence1)
    diffs = []
    for tag, i1, i2, j1, j2 in d.get_opcodes():
        if tag == 'equal':
            continue

        if tag == 'delete':
            diffs.append(
                'Splice out "{0}" at position {1} from the Mutated Sequence'.format(sequence2[i1:i2], i1 + 1))
            continue
        if tag == 'insert':
            diffs.append(
                'Insert "{0}" into Mutated Sequence at position {1}'.format(sequence1[j1:j2], i1 + 1))
            continue
        if tag == 'replace':
            diffs.append(
                'Replace "{0}" in the Mutated Sequence at position {1} with "{2}" from the Original Sequence at position {3}'.format(sequence2[i1:i2], i1 + 1, sequence1[j1:j2], j1 + 1))
            continue    
    
    return diffs


def read_sequence_file(sequence_number):
    sequence_file = open(
        "sequence" + sequence_number + ".txt", "r")
    sequence_file_text = sequence_file.read()
    return sequence_file_text


# def find_start(chars, start_index=0):
#     start_codon_position = -1
#     for index, char in enumerate(chars, start=start_index):
#         if index + 2 > len(chars):
#             break

#         if char == 'a' and chars[index + 1] == 't' and chars[index + 2] == 'g':
#             start_codon_position = index
#             break
#     return start_codon_position


# def find_stop(chars, start_index=-1):
#     end_position = -1
#     start_position = start_index

#     if start_position < 0:
#         return end_position

#     cursor = start_position + 3
#     while cursor + 2 < len(chars):
#         if chars[cursor] == 't' and chars[cursor + 1] == 'g' and chars[cursor + 2] == 'a':
#             end_position = cursor
#             break
#         else:
#             cursor += 3
#     return end_position


# def print_spliced_dna(chars, start_index=0):
#     i = start_index
#     dna_list = []
#     while i < len(chars):
#         cut1 = find_start(dna_sequence, start_index=i)
#         cut2 = find_stop(dna_sequence, start_index=cut1)

#         if cut2 < 0:
#             break
#         i = cut2

#         spliced_dna = ''.join(dna_sequence[cut1:cut2 + 3])
#         print(spliced_dna)
#         dna_list.append(spliced_dna)
#     return dna_list


# def transcribe_dna_to_rna(chars):
#     to_transcribe = []
#     to_transcribe = print_spliced_dna(chars)
#     rna_seq = [item.replace('t', 'u') for item in to_transcribe]
#     return rna_seq


# def find_base_change_mutations(sequence1, sequence2):
#     for index, char in enumerate(sequence1):
#         if sequence2[index] != sequence1[index]:
#             print('Base Change Mutation at position', index + 1,
#                   'from', sequence1[index], 'to', sequence2[index])


# dna_sequence = list(read_sequence_file())
# dna_sequence_for_comparison = list(read_sequence_file())

# print('Spliced Exon(s):')
# print_spliced_dna(dna_sequence)

# print("From DNA to Translational RNA:")
# print(transcribe_dna_to_rna(dna_sequence))

# find_base_change_mutations(dna_sequence, dna_sequence_for_comparison)
# find_insertion_deletion(dna_sequence, dna_sequence_for_comparison)
