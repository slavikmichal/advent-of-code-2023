import java.io.File

fun main() {

    fun getFile(file: String): List<String> {
        return File(file).readLines()
    }

    fun parseLine(line: String): Pair<List<Int>, List<Int>> {
        val (_, numbers) = line.split(":", limit = 2)
        val (winning, current) = numbers.split("|")
        val winNums = winning.trim().split("\\s+".toRegex()).map{ it.toInt() }
        val currentNums = current.trim().split("\\s+".toRegex()).map{ it.toInt() }
        return Pair(winNums, currentNums)
    }

    fun evaluateCard(winning: List<Int>, current: List<Int>): Int {
        var result = 0
        for (win in winning) {
            if (current.contains(win)) {
                result += 1
            }
        }
        return result
    }

    val lines = getFile("4.txt")
    val parsedLines = mutableListOf<Pair<List<Int>, List<Int>>>()
    val cardCounts = mutableListOf<Int>()
    for (line in lines) {
        parsedLines.add(parseLine(line))
        cardCounts.add(1)
    }    
    
    for (index in 0..parsedLines.size - 1) {
        val wins = evaluateCard(parsedLines[index].first, parsedLines[index].second)
        for (w in 0..wins - 1) {
            cardCounts[index + 1 + w] += cardCounts[index]
        }
    }
    var result = cardCounts.sum()
    println(result)
}
