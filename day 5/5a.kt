import java.io.File

fun main() {

    fun getFile(file: String): List<String> {
        return File(file).readLines()
    }

    fun splitAlmanac(lines: List<String>): List<List<String>> {
        val maps = mutableListOf<List<String>>()
        var index = 0
        var loader = mutableListOf<String>()
        for (i in 0..lines.size - 1) {
            if (lines[i] != "") {
                loader.add(lines[i])
            } else {
                maps.add(loader)
                index += 1
                loader = mutableListOf<String>()
            }
        }
        maps.add(loader)
        return maps
    }

    fun getKeyFromMap(input: List<String>, key: Long): Long {
        for (i in 1..input.size - 1) {
            val (dest, source, length) = input[i].trim().split("\\s+".toRegex()).map{ it.toLong() }
            if ((source <= key) && (key <= source + length - 1)) {
                return dest + key - source
            }
        }
        return key
    }

    val lines = getFile("5.txt")
    val almanac = splitAlmanac(lines)
    val seeds = almanac[0][0].split(":")[1].trim().split("\\s+".toRegex()).map{ it.toLong() }

    val locations = mutableListOf<Long>()
    for (seed in seeds) {
        val soilKey = getKeyFromMap(almanac[1], seed)
        val fetilizerKey = getKeyFromMap(almanac[2], soilKey)
        val waterKey = getKeyFromMap(almanac[3], fetilizerKey)
        val lightKey = getKeyFromMap(almanac[4], waterKey)
        val tempKey = getKeyFromMap(almanac[5], lightKey)
        val humidityKey = getKeyFromMap(almanac[6], tempKey)
        val location = getKeyFromMap(almanac[7], humidityKey)
        locations.add(location)
    }
    println(locations.min())
}