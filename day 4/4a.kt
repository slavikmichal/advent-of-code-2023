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
                if (result == 0) {
                    result = 1
                } else {
                    result *= 2
                }
            }
        }
        return result
    }

    val lines = getFile("4.txt")
    val parsedLines = mutableListOf<Pair<List<Int>, List<Int>>>()
    for (line in lines) {
        parsedLines.add(parseLine(line))
    }    
    
    var result = 0
    for (line in parsedLines) {
        val sub = evaluateCard(line.first, line.second)
        result += sub
    }
    println(result)
}
