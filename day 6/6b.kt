import java.io.File

fun main() {

    fun getFile(file: String): List<String> {
        return File(file).readLines()
    }

    fun parseRow(line: String): Long {
        return line.split(":")[1].trim().split("\\s+".toRegex()).map{ it.toLong() }.joinToString(separator="").toLong()
    }

    fun calculateOptions(time: Long, distance: Long): Long {
        var result: Long = 0
        for (t in 0..time) {
            if (t * (time - t) > distance) {
                result += 1
            }
        }
        return result
    }

    val lines = getFile("6.txt")
    val time = parseRow(lines[0])
    val dist = parseRow(lines[1])
    val result = calculateOptions(time, dist)
    println(result)
}