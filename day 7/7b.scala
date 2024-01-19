import scala.io.Source
import scala.collection.mutable.Map
import scala.collection.mutable.ListBuffer
import math.Ordered.orderingToOrdered

object Hello {

    object Rules {
        val cardValues = List("J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A")
    }

    case class Hand(cards: String, value: Long, kinds: List[List[String]] = List.empty[List[String]])

    def getFile(name: String): List[String] = {
        val source = Source.fromFile(name)
        val lines = source.getLines().toList
        source.close()
        lines
    }

    def mapValues(lines: List[String]): List[Hand] = {
        var map = ListBuffer.empty[Hand]
        for (line <- lines) {
            val parsed: Array[String] = line.split("\\s+", 2)
            val kinds = nOfAKind(parsed(0))
            map += Hand(parsed(0), parsed(1).toLong, kinds)
        }
        map.toList
    }

    def nOfAKind(hand: String): List[List[String]] = {
        var ranks = ListBuffer.empty[List[String]]
        for (card <- Rules.cardValues) {
            ranks += card.r.findAllIn(hand).toList
        }
        return ranks.filterNot(l => l.isEmpty).toList
    }

    def getCardRank(card: Char): Int = {
        Rules.cardValues.indexOf(card.toString)
    }

    def getJokeredHand(hand: List[List[String]]): Int = {
        val joinedHand = hand.flatMap(_.mkString).mkString
        val noJ = hand.filterNot(e => e.contains("J")).map(e => (e, e.size)).sortBy(e => (e._2, getCardRank(joinedHand(0)), getCardRank(joinedHand(1)), getCardRank(joinedHand(2)), getCardRank(joinedHand(3)), getCardRank(joinedHand(4)))).reverse.map(e => e._1)
        val numJ = 5 - noJ.map(e => e.size).sum
        if (numJ == 5) {
            return 7
        } 

        val jokered = nOfAKind(joinedHand.replaceAll("J", noJ(0)(0)))
        getHandRank(jokered)
    }

    def getHandRank(hand: List[List[String]]): Int = {
        hand.map(e => e.size).max match
            case 5 => 7
            case 4 => 6
            case 3 => hand.map(e => e.size).sorted.reverse(1) match
                case 2 => 5
                case 1 => 4
            case 2 => hand.map(e => e.size).sorted.reverse(1) match
                case 2 => 3
                case 1 => 2
            case 1 => 1
    }

    def main(args: Array[String]) = {
        val lines = getFile("/Users/slavik/Documents/Fun/advent-of-code-2023/day 7/7.txt")
        val hands = mapValues(lines)
        var result: Long = 0
        val sorted = hands.sortBy(hand => (getJokeredHand(hand.kinds), getCardRank(hand.cards(0)), getCardRank(hand.cards(1)), getCardRank(hand.cards(2)), getCardRank(hand.cards(3)), getCardRank(hand.cards(4))))
        for (index <- 0 to sorted.size - 1) {
            result += (index.toLong + 1) * sorted(index).value
        }
        println(result)
    }
}