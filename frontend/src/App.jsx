import { useState, useEffect } from "react";

function App() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        if (query.trim() === "") return;

        try {
            const res = await fetch(`http://127.0.0.1:8000/search?query=${query}`);
            const data = await res.json();
            setResults(data.results || []);
        } catch (error) {
            console.error("Error fetching data:", error);
            setResults([]);
        }
    };

    useEffect(() => {
        console.log("Updated Results:", results); // ✅ เช็คว่า results เปลี่ยนแปลงจริงไหม
    }, [results]);

    return (
        <div className="search-container">
            <h1> ค้นหาจังหวัด</h1>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="พิมพ์ชื่อจังหวัด..."
            />
            <button onClick={handleSearch}>ค้นหา</button>

            <div>
                {results.length > 0 ? (
                    <ul>
                        {results.map((item, index) => (
                            <li key={index}>
                                <strong>{item.subject}</strong>: {item.object}
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>ไม่มีผลลัพธ์</p>
                )}
            </div>
        </div>
    );
}

export default App;
