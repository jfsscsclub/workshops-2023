const List = (props) => {
  const data = props.data

  const peopleComponents = data.map((person) => {
    console.log(person)
    return (
      <article className="person">
        <img src={person.image} />
        <div>
          <h4>{person.name}</h4>
          <p>{person.age}</p>
        </div>
      </article>
    )
  })

  return peopleComponents
}

export default List
