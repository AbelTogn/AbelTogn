import kotlin.random.Random

fun main() {
    val N = 100
    //val A = aleaTrier(N)
    //println(devinerNombre(N))
    //println(devinerNombreAutomatique(N))
    println(devinerNombreBrut(N))
    //println(aleaTrier(N))
    //println(dichotomie(A, 12))
}

fun devinerNombre(N: Int): Int{
    var demande: Int? = null
    var nbCoup = 0
    val nombre = Random.nextInt(0, N)

    while (demande != nombre){
        print("Devine le nombre: ")
        demande = readLine()?.toInt()
        nbCoup++
        if (demande != null) {
            if (demande < nombre){ println("Trop petit") }

            else if (demande > nombre){ println("Trop grand") }

            else{ break }
        }
    }
    return nbCoup

}

fun devinerNombreAutomatique(N: Int): String{
    var nbCoup = 0
    var minVal = 0
    var maxVal: Int = N
    val reponse: Int = Random.nextInt(0, N)
    var demande: Int?
    var check = true

    while (check){
        demande = (minVal + maxVal) / 2
        nbCoup++

        print("Devine le nombre: $demande || ")

        if (demande < reponse){
            println("Trop petit")
            minVal = demande + 1
        }else if (demande > reponse){
            println("Trop grand")
            maxVal = demande - 1
        }else{ check = false }
    }
    return "Nombre de coups $nbCoup"
}

fun devinerNombreBrut(N: Int): Int{
    var nbCoup = 0
    val nombre: Int = Random.nextInt(0, N)
    var essai: Int = -1

    while (nombre != essai){
        essai++
        nbCoup++
    }
    return nbCoup
}

fun aleaTrier(N: Int): Array<Int>{
    return Array(N) { Random.nextInt(0, 100) }
}

fun dichotomie(A: Array<Int>, x: Int): Boolean{
    println(A)
    if (A.isEmpty()){
        return false
    }else{
        val N: Int = A.size
        var debut = 0
        var fin: Int = N-1

        while (debut <= fin){
            val monIndice: Int = (debut + fin) / 2
            val valeur = A[monIndice]
            debut = if (x == valeur){
                return true
            }else if (valeur < x){
                monIndice + 1
            }else{
                monIndice - 1
            }
        }
    }
    return false
}