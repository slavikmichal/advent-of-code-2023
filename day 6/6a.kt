import java.io.File

fun main() {

    fun getFile(file: String): List<String> {
        return File(file).readLines()
    }

    fun parseRow(line: String): List<Int> {
        return line.split(":")[1].trim().split("\\s+".toRegex()).map{ it.toInt() }
    }

    fun calculateOptions(time: Int, distance: Int): Int {
        var result = 0
        for (t in 0..time) {
            if (t * (time - t) > distance) {
                result += 1
            }
        }
        return result
    }

    val lines = getFile("6.txt")
    val times = parseRow(lines[0])
    val distances = parseRow(lines[1])
    var result = 1
    for (i in 0..times.size-1) {
        val time = times[i]
        val dist = distances[i]

        result *= calculateOptions(time, dist)
    }

    println(result)
}