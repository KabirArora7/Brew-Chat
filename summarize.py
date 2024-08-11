import cohere

co = cohere.Client("Zi5YTS0fMowbQlNZ79RIedVnFAy9cwSMZJ8bZ6Af")


def summarize(interviewText):
    text = (
        "Give three bullet points for a summary of the following conversation (labelled Summary), three bullet points for key insights of the following conversation (labelled key insights), three bullet points for next steps of the following conversation (labelled next steps), and put in three questions one person can ask the other (labelled Questions). Do not state anything afterwards." + str(interviewText)
    )

    response = co.generate(
        prompt=text
    )
    return (response.generations[0].text)