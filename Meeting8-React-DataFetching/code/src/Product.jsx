export default function Product({ data }) {
    return (
      <div className="card">
        <img src={data.img} align="center" />
        <h1>{data.name}</h1>
        <p>${data.price.toFixed(2)}</p>
        <p>{data.description}</p>
      </div>
    )
}