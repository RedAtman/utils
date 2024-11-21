from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def vectorize(texts):
    """Vectorize text using TF-IDF"""
    return TfidfVectorizer().fit_transform(texts).toarray()


def similarity(doc1, doc2):
    """Calculate cosine similarity"""
    return cosine_similarity([doc1, doc2])


def check_plagiarism(vectors, filenames):
    """Check plagiarism between files"""
    plagiarism_results = set()
    for idx_a, vector_a in enumerate(vectors):
        for idx_b, vector_b in enumerate(vectors):
            if idx_a != idx_b:
                sim_score = similarity(vector_a, vector_b)[0][1]
                student_pair = sorted([filenames[idx_a], filenames[idx_b]])
                plagiarism_results.add((sim_score, student_pair[0], student_pair[1]))
    return plagiarism_results


def check_files(files):
    """Read the files and check for plagiarism"""
    student_notes = [open(file, encoding='latin-1').read() for file in files]
    vectors = vectorize(student_notes)
    plagiarism_results = check_plagiarism(vectors, files)
    results = filter(lambda x: x[0] > 0.9, plagiarism_results)
    return list(results)


if __name__ == "__main__":
    import os
    from pathlib import Path

    DATA_DIR = Path('/Users/nut/Dropbox/backup/obsidian/dev')
    files = sorted(filter(lambda x: x.endswith('.md'), os.listdir(DATA_DIR)))
    absolute_files = [DATA_DIR / file for file in files]
    result = check_files(absolute_files)
    print(result)
